from IPython.core.getipython import get_ipython
from io import StringIO
import sys

class NoteBook():
    def __init__(self, drag_setup) -> None:
        pass

    def add_cell(self, text, source='set_next_input', replace=False):
        """
        Add a cell that contain the text var content.
        """
        shell = get_ipython()
        payload = dict(
            source=source,
            text=text,
            replace=replace,
        )
        shell.payload_manager.write_payload(payload, single=False)

    def read_notebook_content(self):
        """
        Read the content of the notebook and return it as a string.
        """
        shell = get_ipython()
        cells = shell.user_ns['In']
        notebook_content = '\n'.join(cells)
        return notebook_content

    def remove_cells_with_substring(self, substring):
        """
        Remove all cells that contain the specified substring.
        """
        shell = get_ipython()
        cells = shell.user_ns['In']
        new_cells = [cell for cell in cells if substring not in cell]
        shell.user_ns['In'] = new_cells

    def execute_code(self, code):
        """
        Execute the provided code. If the code raises an error, return False and the error message.
        Otherwise, return True and the output.
        """
        shell = get_ipython()
        try:
            old_stdout = sys.stdout
            redirected_output = sys.stdout = StringIO()

            exec(code, shell.user_ns)

            sys.stdout = old_stdout

            output = redirected_output.getvalue()
            return True, output
        except Exception as e:
            return False, str(e)