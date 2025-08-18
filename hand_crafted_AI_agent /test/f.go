package main

import "fmt"

func main() {
    // 定义一个数组
    fruits := [4]string{"Apple", "Banana", "Orange", "Mango"}

    // 方法1: 使用索引遍历
    fmt.Println("方法1: 索引遍历")
    for i := 0; i < len(fruits); i++ {
        fmt.Printf("索引 %d: %s\n", i, fruits[i])
    }
}