from unittest import TestCase


class TestUtilsTestCase(TestCase):
    def test_assert_equal(self) -> None:
        from test_amulet_test_utils._test_test_utils import (
            test_assert_equal_1,
            test_assert_equal_2,
            test_assert_equal_3,
            test_assert_equal_4,
            test_assert_equal_5,
            test_assert_equal_6,
        )

        test_assert_equal_1()
        test_assert_equal_2()
        with self.assertRaises(RuntimeError):
            test_assert_equal_3()
        with self.assertRaises(RuntimeError):
            test_assert_equal_4()
        test_assert_equal_5()
        with self.assertRaises(RuntimeError):
            test_assert_equal_6()

    def test_assert_raises(self) -> None:
        from test_amulet_test_utils._test_test_utils import (
            test_assert_raises_1,
            test_assert_raises_2,
            test_assert_raises_3,
        )

        test_assert_raises_1()
        test_assert_raises_2()
        with self.assertRaises(RuntimeError):
            test_assert_raises_3()
