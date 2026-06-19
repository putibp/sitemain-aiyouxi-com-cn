from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

BASE_URL = "https://sitemain-aiyouxi.com.cn"
CORE_KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    """
    Represents a structured note for a keyword.
    """
    keyword: str
    title: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None
    source_url: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_note_brief(note: KeywordNote) -> str:
    """
    Returns a short one-line summary of the note.
    """
    tag_str = ", ".join(note.tags) if note.tags else "无标签"
    return f"[{note.keyword}] {note.title} ({tag_str})"


def format_note_detail(note: KeywordNote) -> str:
    """
    Returns a detailed multi-line formatted string for a note.
    """
    lines = [
        f"关键词：{note.keyword}",
        f"标题：{note.title}",
        f"内容：{note.content}",
        f"标签：{', '.join(note.tags) if note.tags else '无'}",
        f"创建时间：{note.created_at}",
        f"来源：{note.source_url or '无'}",
        "---",
    ]
    return "\n".join(lines)


def format_all_notes_as_report(notes: List[KeywordNote]) -> str:
    """
    Generates a full report string from a list of KeywordNote objects.
    """
    header = f"关键词笔记报告（核心：{CORE_KEYWORD}）\n来源：{BASE_URL}\n"
    separator = "=" * 50
    parts = [header, separator]
    for i, note in enumerate(notes, 1):
        brief = format_note_brief(note)
        detail = format_note_detail(note)
        parts.append(f"笔记 #{i}: {brief}")
        parts.append(detail)
    return "\n".join(parts)


# --- Example data using provided URL and keyword ---
def get_example_notes() -> List[KeywordNote]:
    """
    Returns a list of sample KeywordNote objects for demonstration.
    """
    note1 = KeywordNote(
        keyword=CORE_KEYWORD,
        title="爱游戏平台简介",
        content="爱游戏是一个专注于游戏内容分享的在线平台，提供最新游戏资讯与评测。",
        tags=["游戏", "平台", "资讯"],
        source_url=f"{BASE_URL}/about",
    )
    note2 = KeywordNote(
        keyword=CORE_KEYWORD,
        title="热门游戏推荐",
        content="本周爱游戏推荐五款独立游戏佳作，涵盖动作、解谜与角色扮演类型。",
        tags=["推荐", "独立游戏"],
        source_url=f"{BASE_URL}/hot",
    )
    note3 = KeywordNote(
        keyword="游戏攻略",
        title="如何快速上手新游戏",
        content="在爱游戏社区中，玩家分享了多条实用攻略，帮助新手快速掌握技巧。",
        tags=["攻略", "新手"],
        source_url=f"{BASE_URL}/guide",
    )
    return [note1, note2, note3]


if __name__ == "__main__":
    print("运行 keyword_notes.py 示例\n")
    sample_notes = get_example_notes()
    report = format_all_notes_as_report(sample_notes)
    print(report)