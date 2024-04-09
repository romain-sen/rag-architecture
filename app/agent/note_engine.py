from llama_index.core.tools import FunctionTool
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
note_path = os.path.join(base_dir, "data", "note.txt")


def save_note(note: str):
    if not os.path.exists(note_path):
        open(note_path, "w")

    with open(note_path, "a") as f:
        f.write({note + "\n"})

    return "Note saved."


note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user",
)
