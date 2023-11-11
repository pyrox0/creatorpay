# SPDX-License-Identifier: MPL-2.0-no-copyleft-exception
{
  description = "Python version of I/O, Pyrox's Helper bot!";
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  inputs.flake-parts.url = "github:hercules-ci/flake-parts";
  inputs.devenv.url = "github:cachix/devenv";
  inputs.pre-commit-hooks-nix.url = "github:cachix/pre-commit-hooks.nix";
  inputs.treefmt-nix.url = "github:numtide/treefmt-nix";
  inputs.treefmt-nix.inputs.nixpkgs.follows = "nixpkgs";

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      imports = [
        inputs.devenv.flakeModule
        inputs.pre-commit-hooks-nix.flakeModule
        inputs.treefmt-nix.flakeModule
      ];
      flake = {
        # Put your original flake attributes here.
      };
      systems = [
        # systems for which you want to build the `perSystem` attributes
        "x86_64-linux"
        # ...
      ];
      perSystem = {
        config,
        pkgs,
        ...
      }: {
        devenv.shells.default = {
          name = "io_bot-shell";
          packages = [config.treefmt.build.wrapper pkgs.gcc pkgs.ruff];
          languages.nix.enable = true;
          languages.python.enable = true;
          languages.python.package = pkgs.python311;
          languages.python.poetry.enable = true;
          languages.python.venv.enable = true;
          pre-commit = {
            hooks = {
              black.enable = false;
              ruff.enable = true;
            };
          };
        };
        pre-commit = {
          check.enable = true;
        };
        treefmt = {
          flakeFormatter = true;
          projectRootFile = "flake.nix";
          programs = {
            alejandra.enable = true;
            black.enable = true;
            deadnix.enable = true;
          };
          settings.formatter = {
            ruff = {
              command = pkgs.ruff;
              includes = ["*.py"];
            };
          };
        };
      };
    };
}
