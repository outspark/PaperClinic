from pathlib import Path

from jinja2 import Template

from src.utils.yaml_loader import load_yaml


class PromptManager:
    def __init__(self, prompts_path: Path | str) -> None:
        self._raw = load_yaml(prompts_path)

    def render_user(self, key: str, **variables: str) -> str:
        block = self._raw[key]
        tpl = Template(block["user_template"], trim_blocks=True)
        return tpl.render(**variables)

    def system_prompt(self, key: str) -> str:
        return str(self._raw[key]["system"]).strip()
