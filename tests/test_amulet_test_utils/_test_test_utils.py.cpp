#include <pybind11/pybind11.h>

#include <stdexcept>
#include <string>

#include <amulet/test_utils/test_utils.hpp>

namespace py = pybind11;

static void test_assert_equal_1()
{
    ASSERT_EQUAL(bool, 0, 0)
}
static void test_assert_equal_2()
{
    ASSERT_EQUAL(bool, 1, 1)
}
static void test_assert_equal_3()
{
    ASSERT_EQUAL(bool, 0, 1)
}
static void test_assert_equal_4()
{
    ASSERT_EQUAL(bool, 1, 0)
}

static void test_assert_equal_5()
{
    ASSERT_EQUAL(std::string, "hello world", "hello world")
}

static void test_assert_equal_6()
{
    ASSERT_EQUAL(std::string, "hello world", "hello world!")
}

static void test_assert_not_equal(int a, int b)
{
    ASSERT_NOT_EQUAL(int, a, b);
}

static void test_assert_less(int a, int b)
{
    ASSERT_LESS(int, a, b);
}

static void test_assert_less_equal(int a, int b)
{
    ASSERT_LESS_EQUAL(int, a, b);
}

static void test_assert_greater(int a, int b)
{
    ASSERT_GREATER(int, a, b);
}

static void test_assert_greater_equal(int a, int b)
{
    ASSERT_GREATER_EQUAL(int, a, b);
}

static void test_assert_raises_1()
{
    ASSERT_RAISES(std::runtime_error, throw std::runtime_error(""))
}

static void test_assert_raises_2()
{
    ASSERT_RAISES(std::exception, throw std::runtime_error(""))
}

static void test_assert_raises_3() {
    ASSERT_RAISES(std::runtime_error, throw std::invalid_argument(""))
}

static void test_assert_almost_equal(double a, double b){
    ASSERT_ALMOST_EQUAL(double, a, b);
}

static void test_assert_almost_equal_2(double a, double b, double err){
    ASSERT_ALMOST_EQUAL_2(double, a, b, err);
}

static void test_assert_not_almost_equal(double a, double b){
    ASSERT_NOT_ALMOST_EQUAL(double, a, b);
}

static void test_assert_not_almost_equal_2(double a, double b, double err){
    ASSERT_NOT_ALMOST_EQUAL_2(double, a, b, err);
}

PYBIND11_MODULE(_test_test_utils, m)
{
    m.def("test_assert_equal_1", &test_assert_equal_1);
    m.def("test_assert_equal_2", &test_assert_equal_2);
    m.def("test_assert_equal_3", &test_assert_equal_3);
    m.def("test_assert_equal_4", &test_assert_equal_4);
    m.def("test_assert_equal_5", &test_assert_equal_5);
    m.def("test_assert_equal_6", &test_assert_equal_6);
    m.def("test_assert_not_equal", &test_assert_not_equal);
    m.def("test_assert_less", &test_assert_less);
    m.def("test_assert_less_equal", &test_assert_less_equal);
    m.def("test_assert_greater", &test_assert_greater);
    m.def("test_assert_greater_equal", &test_assert_greater_equal);
    m.def("test_assert_raises_1", &test_assert_raises_1);
    m.def("test_assert_raises_2", &test_assert_raises_2);
    m.def("test_assert_raises_3", &test_assert_raises_3);
    m.def("test_assert_almost_equal", &test_assert_almost_equal);
    m.def("test_assert_almost_equal_2", &test_assert_almost_equal_2);
    m.def("test_assert_not_almost_equal", &test_assert_not_almost_equal);
    m.def("test_assert_not_almost_equal_2", &test_assert_not_almost_equal_2);
}
