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

    def test_assert_not_equal(self) -> None:
        from test_amulet_test_utils._test_test_utils import test_assert_not_equal
        test_assert_not_equal(5, 6)
        test_assert_not_equal(6, 5)
        with self.assertRaises(RuntimeError):
            test_assert_not_equal(5, 5)
        with self.assertRaises(RuntimeError):
            test_assert_not_equal(6, 6)

    def test_assert_less(self) -> None:
        from test_amulet_test_utils._test_test_utils import test_assert_less
        test_assert_less(5, 6)
        with self.assertRaises(RuntimeError):
            test_assert_less(5, 5)

    def test_assert_less_equal(self) -> None:
        from test_amulet_test_utils._test_test_utils import test_assert_less_equal
        test_assert_less_equal(5, 6)
        test_assert_less_equal(5, 5)
        with self.assertRaises(RuntimeError):
            test_assert_less_equal(6, 5)

    def test_assert_greater(self) -> None:
        from test_amulet_test_utils._test_test_utils import test_assert_greater
        test_assert_greater(6, 5)
        with self.assertRaises(RuntimeError):
            test_assert_greater(5, 5)

    def test_assert_greater_equal(self) -> None:
        from test_amulet_test_utils._test_test_utils import test_assert_greater_equal
        test_assert_greater_equal(6, 5)
        test_assert_greater_equal(5, 5)
        with self.assertRaises(RuntimeError):
            test_assert_greater_equal(5, 6)

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
