
#include <iostream>
#include <string>
#include <pybind11/pybind11.h>


// 抽象基底クラス
class CatBase {
protected:
    // メンバ変数（protected に変更）
    std::string name_;

public:
    // コンストラクタ（修正: 初期化リストに {} を追加）
    CatBase(const std::string& name) : name_(name) {}

    // 純粋仮想関数
    virtual void say() = 0;

    // 仮想デストラクタ
    virtual ~CatBase() = default;
};