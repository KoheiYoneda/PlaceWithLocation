#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 kohei <nsshowdream@gmail.com>

import csv
import googlemaps

# リストを渡すとCSVファイルとして書き出してくれる関数
def writeCSV(list):
    f = open('output2.csv', 'w')
    writer = csv.writer(f)
    writer.writerows(list)
    f.close()

# 地名を渡すと住所を返す関数
def wordToAddress(word):
    googleMaps = googlemaps.Client(key="****")
    geocodeResult = googleMaps.geocode(word,language="ja")
    try:
        geocodeResultDict = geocodeResult[0]
        address = geocodeResultDict["formatted_address"]
        return address
    except:
        return "error"

# メイン関数
def main():
    with open('Noun.place.csv', 'r') as f:
        reader = csv.reader(f)
        counter = 0 # データ数のカウンタ
        placeWithLocationList = []
        for row in reader:
            place = row[0] # Noun.place.csvの各行の1つ目のデータが地名
            address = wordToAddress(place)
            address = address.replace("日本, ","") # 住所文字列から「日本,」を削除
            address = address.replace("\"","") # 住所文字列から「"」を削除
            placeWithLocation = [place,address]
            if address!='error':
                placeWithLocationList.append(placeWithLocation)
                counter += 1
            print counter
            print place,address
            if(counter>10000):
            	break

        # 完成した[地名,住所]のリストをCSVファイルに書き出す
        writeCSV(placeWithLocationList)
        # データ数を表示
        print counter

if __name__ == '__main__':
    main()


