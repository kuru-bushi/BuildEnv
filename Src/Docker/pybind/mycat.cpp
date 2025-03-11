#include <iostream>
#include <string>
#include "mycat.h"

#include <pybind11/pybind11.h>
namespace py = pybind11;

// 派生クラス
class Cat : public CatBase {
public:
    // 基底クラスのコンストラクタを正しく呼び出す
    Cat(const std::string& name) : CatBase(name) {}

    // 純粋仮想関数のオーバーライド
    void say() override {
        std::cout << name_ << " said meow." << std::endl;
    }

    // デストラクタのオーバーライド（省略可能）
    ~Cat() override {}
};

// class Cat{
//     Cat() {};
// }

PYBIND11_MODULE(mycat, m) {
    py::class_<Cat>(m, "Cat")
        .def(py::init<const std::string&>())
        .def("say", &Cat::say)
        ;
}