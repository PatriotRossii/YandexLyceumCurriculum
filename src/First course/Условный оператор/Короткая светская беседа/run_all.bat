csc solution.cs
solution.exe
del /f solution.exe

ghc solution.hs
solution.exe
del /f solution.hi
del /f solution.o

python solution.py

cargo run --manifest-path "solution/Cargo.toml" -q
del /f solution.exe