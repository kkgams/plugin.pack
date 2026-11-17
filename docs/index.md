---
title: plugin.pack
description: Rectangle packing.
status: reference
---

# plugin.pack

Rectangle packing for [GAMS](https://github.com/kkgams/gams).

| Unit | Source | Original work |
| --- | --- | --- |
| Pack component | `plugins/pack.comp/` | GAMS contributors; stb_rect_pack by Sean Barrett |

## Development

Use the pinned toolchain with `nix develop --command make <target>`.

| Command | Purpose |
| --- | --- |
| `make test` | Run native Wasmtime packing/error assertions. |
| `make build` | Compile the C/WASI component with embedded complete terms. |
| `make package` | Build `build.nosync/plugin.pack.wasm`, `LICENSES.zip` and `SHA256SUMS`. |
| `make open` | Build and open the local Project in the released macOS Apple Silicon Host. |
| `make docs` | Build the pinned wiki in `build.nosync/site/`. |
| `make serve-docs` | Serve docs; independent `DOCS_PORT` defaults to 8080. |
| `make validate-docs` | Validate wiki content. |
| `make clean` | Remove all of `build.nosync/`, `tools/` and `gams_modules/`, including unmarked contents; refuse tracked files and symlinks before deleting anything. |

The local Files View browses the Project; it is not a packing editor. First launch downloads pinned supporting Units. An existing Host is never updated implicitly. `make test` runs existing packing/error assertions on a separately compiled test component using pinned native Wasmtime and Python unittest. These bounded tests do not establish full API or Host integration coverage.

## API

Exports `gams:pack/pack@1.0.0`, world `pack-plugin`. `pack(request)` accepts atlas dimensions, padding, auto-size and rectangles with optional IDs. Results include positions, dimensions, per-rectangle success and packed/failed counts; errors have typed code/message. Complete types are in `plugins/pack.comp/wit/package.wit`.
