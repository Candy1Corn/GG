package main

// www.nowcoder.com, https://www.nowcoder.com , ac.nowcoder.com

import (
	"fmt"
	"strings"
)

func main() {
	var name string
	fmt.Print("請輸入網址：")
	fmt.Scanln(&name) //有沒有「&」有差 !!!

	if strings.Contains("https://", name) {
		f1 := strings.Split(name, "//")[1]
		f2 := strings.Split(f1, ".")[0]
		if f2 == "www" {
			println("NewCoder ! ")
		} else if f2 == "ac" {
			println("Ac ! ")
		} else {
			println("唉呀 ~ 中秋節快樂 ! ")
		}
	} else {
		f3 := strings.Split(name, ".")[0]
		if f3 == "www" {
			println("NewCoder ! ")
		} else if f3 == "ac" {
			println("Ac ! ")
		} else {
			println("唉呀 ~ 中秋節快樂 ! ")
		}
	}
}
