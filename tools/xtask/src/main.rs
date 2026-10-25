//! xtask: automatización del repositorio 101Agents (101 Engine).
//!
//! Implementa el binario detrás del alias `cargo xtask` (definido en
//! `.cargo/config.toml`) y centraliza las tareas repetitivas del flujo de
//! trabajo del estudio: verificación completa antes de abrir un PR
//! (`check`), pruebas de un crate concreto (`test <crate>`) y, en tareas
//! futuras, escenarios dorados, benchmarks, validación de contenido,
//! campañas de 101 Lab y generación de documentación.
//!
//! Es una herramienta de soporte, no un crate de simulación: solo depende
//! de `std` y no le aplican las reglas de determinismo del motor.

use std::io::ErrorKind;
use std::process::{Command, ExitCode};

/// Texto de uso, en español, con todos los subcomandos disponibles.
const USAGE: &str = "uso: cargo xtask <comando> [argumentos]

Comandos:
  check         Formato, clippy, pruebas y licencias/seguridad (antes de abrir un PR).
  test <crate>  Pruebas de un único crate del workspace.
  golden        Escenarios dorados de determinismo (tarea T-111).
  bench         Benchmarks comparados con la rama principal (sin asignar).
  data          Compila y valida el contenido de games/epoch/data (tarea T-202).
  lab           Campañas cortas de 101 Lab (tarea T-216).
  docs          Genera la documentación de los crates (sin asignar).
  help          Muestra esta ayuda.
";

/// Petición interpretada de los argumentos de la línea de comandos.
///
/// Separar el análisis (`parse`) de la ejecución (`dispatch`) permite probar
/// el primero con pruebas unitarias sin lanzar procesos externos.
#[derive(Debug, Clone, PartialEq, Eq)]
enum Request {
    /// `check`: verificación completa (fmt, clippy, test, cargo-deny).
    Check,
    /// `test <crate>`: pruebas de un único crate del workspace.
    Test { krate: String },
    /// Ayuda explícita: `help`, `-h` o `--help`.
    Help,
    /// No se pasó ningún subcomando.
    NoCommand,
    /// Subcomando o argumentos no válidos, con el motivo.
    Invalid(String),
    /// Escenarios dorados de determinismo (tarea T-111).
    Golden,
    /// Benchmarks (sin asignar; Anexo F del documento maestro).
    Bench,
    /// Validación del contenido de `games/epoch/data` (tarea T-202).
    Data,
    /// Campañas de 101 Lab (tarea T-216).
    Lab,
    /// Documentación de crates (sin asignar).
    Docs,
}

/// Un paso de la verificación: cabecera legible y comando a ejecutar.
struct Step<'a> {
    /// Cabecera que se imprime antes de lanzar el comando.
    title: &'a str,
    /// Programa que se ejecuta.
    program: &'a str,
    /// Argumentos del programa.
    args: &'a [&'a str],
}

impl<'a> Step<'a> {
    /// Construye un paso a partir de su cabecera, programa y argumentos.
    fn new(title: &'a str, program: &'a str, args: &'a [&'a str]) -> Self {
        Self {
            title,
            program,
            args,
        }
    }

    /// Ejecuta el paso heredando stdout y stderr (sin captura) y devuelve
    /// `true` solo si el proceso terminó con éxito. Antes de lanzarlo
    /// imprime una cabecera `== <título>` para seguir la salida con facilidad.
    fn run(&self) -> bool {
        println!("== {}", self.title);
        match Command::new(self.program).args(self.args).status() {
            Ok(status) if status.success() => true,
            Ok(status) => {
                eprintln!(
                    "xtask: el paso \"{}\" falló con estado {status}",
                    self.title
                );
                false
            }
            Err(err) => {
                eprintln!("xtask: no se pudo ejecutar \"{}\": {err}", self.program);
                false
            }
        }
    }
}

/// Punto de entrada: interpreta los argumentos y ejecuta la petición.
fn main() -> ExitCode {
    let args: Vec<String> = std::env::args().skip(1).collect();
    dispatch(parse(&args))
}

/// Interpreta los argumentos (sin el nombre del binario) y devuelve la
/// petición correspondiente. Es una función pura: no ejecuta procesos.
fn parse(args: &[String]) -> Request {
    let Some((first, rest)) = args.split_first() else {
        return Request::NoCommand;
    };
    match first.as_str() {
        "check" => Request::Check,
        "test" => match rest {
            [krate] => Request::Test {
                krate: krate.clone(),
            },
            _ => Request::Invalid(
                "\"test\" exige exactamente un argumento: el nombre del crate".to_string(),
            ),
        },
        "golden" => Request::Golden,
        "bench" => Request::Bench,
        "data" => Request::Data,
        "lab" => Request::Lab,
        "docs" => Request::Docs,
        "help" | "-h" | "--help" => Request::Help,
        unknown => Request::Invalid(format!("comando desconocido: {unknown}")),
    }
}

/// Ejecuta una petición y devuelve el código de salida del binario.
fn dispatch(request: Request) -> ExitCode {
    match request {
        Request::Check => cmd_check(),
        Request::Test { krate } => cmd_test(&krate),
        Request::Golden => not_implemented("tarea T-111 (escenarios dorados)"),
        Request::Bench => not_implemented("tarea T-XXX (sin asignar; benchmarks, Anexo F)"),
        Request::Data => not_implemented("tarea T-202 (validación de contenido)"),
        Request::Lab => not_implemented("tarea T-216 (101 Lab)"),
        Request::Docs => not_implemented("tarea T-XXX (sin asignar; documentación de crates)"),
        Request::Help => {
            print!("{USAGE}");
            ExitCode::SUCCESS
        }
        Request::NoCommand => {
            eprintln!("error: no se especificó ningún comando");
            eprint!("{USAGE}");
            ExitCode::FAILURE
        }
        Request::Invalid(reason) => {
            eprintln!("error: {reason}");
            eprint!("{USAGE}");
            ExitCode::FAILURE
        }
    }
}

/// Verificación completa del workspace, en orden y deteniéndose en el primer
/// paso que falle: formato, clippy, pruebas y licencias/seguridad.
fn cmd_check() -> ExitCode {
    let steps = [
        Step::new("cargo fmt --check", "cargo", &["fmt", "--check"]),
        Step::new(
            "cargo clippy --workspace --all-targets -- -D warnings",
            "cargo",
            &[
                "clippy",
                "--workspace",
                "--all-targets",
                "--",
                "-D",
                "warnings",
            ],
        ),
        Step::new("cargo test --workspace", "cargo", &["test", "--workspace"]),
    ];
    for step in &steps {
        if !step.run() {
            return ExitCode::FAILURE;
        }
    }
    if !cargo_deny_available() || !Step::new("cargo deny check", "cargo", &["deny", "check"]).run()
    {
        return ExitCode::FAILURE;
    }
    ExitCode::SUCCESS
}

/// Ejecuta las pruebas de un único crate mediante `cargo test -p <crate>`.
fn cmd_test(krate: &str) -> ExitCode {
    let title = format!("cargo test -p {krate}");
    let args = ["test", "-p", krate];
    let step = Step::new(&title, "cargo", &args);
    if step.run() {
        ExitCode::SUCCESS
    } else {
        ExitCode::FAILURE
    }
}

/// Comprueba que `cargo-deny` está instalado lanzando `cargo-deny --version`.
///
/// Si el ejecutable no se encuentra, imprime por stderr cómo instalarlo y
/// devuelve `false` para que `check` aborte sin continuar. Cualquier otro
/// error de arranque también se considera fallo.
fn cargo_deny_available() -> bool {
    println!("== cargo-deny --version");
    match Command::new("cargo-deny").arg("--version").status() {
        Ok(_) => true,
        Err(err) if err.kind() == ErrorKind::NotFound => {
            eprintln!(
                "cargo-deny no está instalado; instálalo con `cargo install cargo-deny --locked`"
            );
            false
        }
        Err(err) => {
            eprintln!("xtask: no se pudo ejecutar cargo-deny: {err}");
            false
        }
    }
}

/// Mensaje y código de salida comunes a los subcomandos pendientes: imprime
/// la tarea que lo implementará por stderr y devuelve fallo.
fn not_implemented(pending: &str) -> ExitCode {
    eprintln!("no implementado: {pending}");
    ExitCode::FAILURE
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Convierte literales en la lista de argumentos que espera `parse`.
    fn args(values: &[&str]) -> Vec<String> {
        values.iter().map(|value| (*value).to_string()).collect()
    }

    /// `parse` reconoce todos los subcomandos y rechaza los desconocidos o
    /// mal argumentados, sin ejecutar ningún proceso externo.
    #[test]
    fn parse_recognizes_subcommands() {
        assert_eq!(parse(&args(&["check"])), Request::Check);
        assert_eq!(
            parse(&args(&["test", "e101-store"])),
            Request::Test {
                krate: "e101-store".to_string()
            }
        );
        assert_eq!(parse(&args(&["--help"])), Request::Help);
        assert_eq!(parse(&args(&["help"])), Request::Help);
        assert_eq!(parse(&args(&["golden"])), Request::Golden);
        assert_eq!(parse(&Vec::new()), Request::NoCommand);
        assert_eq!(
            parse(&args(&["start"])),
            Request::Invalid("comando desconocido: start".to_string())
        );
        assert!(matches!(parse(&args(&["test"])), Request::Invalid(_)));
        assert!(matches!(
            parse(&args(&["test", "a", "b"])),
            Request::Invalid(_)
        ));
    }

    /// Los stubs de tareas pendientes siempre devuelven fallo.
    #[test]
    fn stubs_fail() {
        assert_eq!(
            not_implemented("tarea T-111 (escenarios dorados)"),
            ExitCode::FAILURE
        );
    }

    /// El texto de uso documenta todos los subcomandos del binario.
    #[test]
    fn usage_documents_every_subcommand() {
        for command in ["check", "test", "golden", "bench", "data", "lab", "docs"] {
            assert!(
                USAGE.contains(command),
                "falta {command} en el texto de uso"
            );
        }
    }
}
