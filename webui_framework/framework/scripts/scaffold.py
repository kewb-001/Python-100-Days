from argparse import ArgumentParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def snake_case(name: str) -> str:
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def validate_name(name: str):
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name):
        raise ValueError("name must start with a letter and contain only letters, digits, underscore")


def page_template(class_name: str) -> str:
    return f'''from framework.core.base_page import BasePage\n\n\nclass {class_name}Page(BasePage):\n    def __init__(self, page):\n        super().__init__(page)\n\n    # locators\n\n    # actions\n'''


def flow_template(class_name: str) -> str:
    return f'''class {class_name}Flow:\n    def __init__(self, page):\n        self.page = page\n\n    def run(self):\n        raise NotImplementedError\n'''


def test_template(module_name: str) -> str:
    return f'''import pytest\n\n\ndef test_{module_name}_smoke(page):\n    page.set_content("<h1>{module_name}</h1>")\n    assert page.locator("h1").inner_text() == "{module_name}"\n'''


def write_file(output: Path, content: str, force: bool):
    if output.exists() and not force:
        raise FileExistsError(f"{output} already exists; use --force to overwrite")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content + "\n", encoding="utf-8")


def main():
    parser = ArgumentParser(description="Scaffold generator")
    parser.add_argument("kind", choices=["page", "component", "flow", "test"])
    parser.add_argument("name")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    validate_name(args.name)
    name = args.name

    if args.kind in {"page", "component"}:
        folder = "pages" if args.kind == "page" else "components"
        file_name = f"{snake_case(name)}_{args.kind}.py"
        output = ROOT / "framework" / folder / file_name
        write_file(output, page_template(name), args.force)
    elif args.kind == "flow":
        output = ROOT / "framework" / "flows" / f"{snake_case(name)}_flow.py"
        write_file(output, flow_template(name), args.force)
    else:
        module_name = snake_case(name)
        output = ROOT / "tests" / f"test_{module_name}.py"
        write_file(output, test_template(module_name), args.force)

    print(f"created: {output}")


if __name__ == "__main__":
    main()
