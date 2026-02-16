from pathlib import Path;

des_dir=Path("./dir1")

if not des_dir.exists():
    des_dir.mkdir()

src_file=Path("./Sample_data/README.md")
dest_file=des_dir / "README.md"
src_file.rename(dest_file)
    