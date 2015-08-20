import unittest
import logging

log = logging.getLogger(__name__)


class TestDynamicTaskLoading(unittest.TestCase):

    def test_sanity_dynamic_task_loading(self):
        import pbsmrtpipe.loader as D
        meta_tasks = D.load_all_tool_contracts()
        for meta_task in meta_tasks.values():
            log.debug("\n" + meta_task.summary())

        self.assertIsNotNone(meta_tasks)
