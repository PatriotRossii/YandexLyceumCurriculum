csc solution.cs >nul 2>&1
solution.exe

ghc solution.hs >nul 2>&1
solution.exe
del /f solution.hi
del /f solution.o

python solution.py

cargo run --manifest-path "solution/Cargo.toml" -q
del /f solution.exe