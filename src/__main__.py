import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Stow package management utility.")

    # Options
    parser.add_argument(
        "-d",
        "--dir",
        type=str,
        default=os.environ.get("STOW_DIR", os.getcwd()),
        help="Set the stow directory to dir. Defaults to STOW_DIR or current directory.",
    )
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        help="Set the target directory to dir, overriding the default of the parent of the stow directory.",
    )
    parser.add_argument(
        "--ignore",
        type=str,
        action="append",
        default=[],
        help="Suppress acting on files that match the given regex. Can be repeated.",
    )
    parser.add_argument(
        "--defer",
        type=str,
        action="append",
        default=[],
        help="Avoid stowing files matching the regex if they are already stowed by another package. Can be repeated.",
    )
    parser.add_argument(
        "--override",
        type=str,
        action="append",
        default=[],
        help="Force stowing files matching the regex, even if already stowed. Can be repeated.",
    )
    parser.add_argument(
        "--dotfiles",
        action="store_true",
        help="Enable special handling for dotfiles by replacing a dot- prefix with a . when creating symlinks.",
    )
    parser.add_argument(
        "--no-folding",
        action="store_true",
        help="Disable tree folding; creates symlinks for directories instead of a single symlink.",
    )
    parser.add_argument(
        "--adopt",
        action="store_true",
        help="Move existing plain files in the target directory into the stow package.",
    )
    parser.add_argument(
        "-n",
        "--no",
        "--simulate",
        action="store_true",
        help="Simulate the operations without modifying the filesystem.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        type=int,
        nargs="?",
        const=1,
        default=0,
        help="Enable verbose output. Increase verbosity with each -v, or set a specific level with --verbose=n.",
    )
    parser.add_argument(
        "-p",
        "--compat",
        action="store_true",
        help="Scan the entire target tree when unstowing, restoring legacy behavior.",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="Stow version 1.0",
        help="Display the version number of Stow and exit.",
    )
    parser.add_argument(
        "-h", "--help", action="help", help="Show the command syntax and exit."
    )

    # Action Flags
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument(
        "-D",
        "--delete",
        nargs="+",
        help="Delete (unstow) the specified package(s) from the target directory.",
    )
    action_group.add_argument(
        "-R",
        "--restow",
        nargs="+",
        help="Restow the specified package(s) by first unstowing and then stowing them again.",
    )
    action_group.add_argument(
        "-S",
        "--stow",
        nargs="+",
        help="Explicitly stow the specified package(s) that follow this option.",
    )

    args = parser.parse_args()

    # Here you can add the logic to handle the parsed arguments as per your application's requirements.

    # Example output to demonstrate captured arguments:
    print("Stow Directory:", args.dir)
    print("Target Directory:", args.target)
    print("Ignored patterns:", args.ignore)
    print("Deferred patterns:", args.defer)
    print("Overridden patterns:", args.override)
    print("Dotfiles handling enabled:", args.dotfiles)
    print("No folding enabled:", args.no_folding)
    print("Adopt mode enabled:", args.adopt)
    print("Simulation mode:", args.no)
    print("Verbose level:", args.verbose)
    print("Compatibility mode:", args.compat)

    if args.delete:
        print("Deleting packages:", args.delete)
    if args.restow:
        print("Restowing packages:", args.restow)
    if args.stow:
        print("Stowing packages:", args.stow)


if __name__ == "__main__":
    main()
