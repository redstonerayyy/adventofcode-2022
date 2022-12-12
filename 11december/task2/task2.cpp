#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm> 
#include <cctype>
#include <locale>
#include <cmath>

#include <boost/multiprecision/cpp_int.hpp>

namespace util {
    std::vector<std::string> split(std::string stringtosplit, std::string delimiter) {
        std::vector<std::string> parts;        
        size_t pos = 0;
        while ((pos = stringtosplit.find(delimiter)) != std::string::npos) {
            parts.emplace_back(stringtosplit.substr(0, pos));
            stringtosplit.erase(0, pos + delimiter.length());
        }
        if(stringtosplit.length() > 0){
            parts.emplace_back(stringtosplit);
        }
        return parts;
    }

    std::string replace(std::string stringtoreplace, std::string oldpart, std::string newpart){
        size_t pos = 0;
        int sublength = oldpart.length();
        while((pos = stringtoreplace.find(oldpart)) != std::string::npos){
            stringtoreplace = stringtoreplace.replace(pos, sublength, newpart);
        }
        return stringtoreplace;
    }

    //https://stackoverflow.com/questions/216823/how-to-trim-an-stdstring
    // trim from start (in place)
    static inline void ltrim(std::string &s) {
        s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](unsigned char ch) {
            return !std::isspace(ch);
        }));
    }

    // trim from end (in place)
    static inline void rtrim(std::string &s) {
        s.erase(std::find_if(s.rbegin(), s.rend(), [](unsigned char ch) {
            return !std::isspace(ch);
        }).base(), s.end());
    }

    // trim from both ends (in place)
    static inline void trim(std::string &s) {
        rtrim(s);
        ltrim(s);
    }
}

struct Monkey {
    int monkeyid;
    std::vector<boost::multiprecision::cpp_int> monkeyitems;
    std::string operationsign;
    std::string operationnumber;
    int monkeydivtestnumber;
    int monkeytrue;
    int monkeyfalse;
    int inspectioncount;
};

int main(){
    // read file line by line
    std::string line;
    std::ifstream file("test.txt");

    std::vector<std::string> lines;
    while(std::getline(file, line)){
        util::trim(line);
        if(line != ""){
            lines.push_back(line);
        }
    }

    // convert 6 lines to 1 monkey
    std::vector<Monkey> monkeys;

    for(int i = 0; i < lines.size(); i += 6){
        Monkey newmonkey;
        // id of monkey, should be unique from input counting up from 0
        newmonkey.monkeyid = std::stoi(util::replace(util::split(lines.at(i), " ").at(1), ";", ""));    
        // items
        std::vector<std::string> partsitems = util::split(lines.at(i + 1), " ");
        for(int j = 2; j < partsitems.size(); ++j){
            newmonkey.monkeyitems.emplace_back(std::stoi(partsitems[j]));
        }
        // operation
        newmonkey.operationsign = util::split(lines.at(i + 2), " ").at(4);
        newmonkey.operationnumber = util::split(lines.at(i + 2), " ").at(5);
        // test and possible monkeys to transfer item to
        newmonkey.monkeydivtestnumber = std::stoi(util::split(lines.at(i + 3), " ").at(util::split(lines.at(i + 3), " ").size() - 1));
        newmonkey.monkeytrue = std::stoi(util::split(lines.at(i + 4), " ").at(util::split(lines.at(i + 4), " ").size() - 1));
        newmonkey.monkeyfalse = std::stoi(util::split(lines.at(i + 5), " ").at(util::split(lines.at(i + 5), " ").size() - 1));
        newmonkey.inspectioncount = 0;
        monkeys.push_back(newmonkey);
    }

    for(auto monkey : monkeys){
        std::cout << monkey.monkeyid << " ";
        for(auto item : monkey.monkeyitems){
            std::cout << item << " ";
        }
        std::cout << "\n";
    }
    // apply rounds
    int rounds = 20;
    for(int round = 0; round < rounds; ++round){
        if(round % 100 == 0){
            std::cout << round << std::endl;
        }
        for(int mindex = 0; mindex < monkeys.size(); ++mindex){
            for(int itemindex = 0; itemindex < monkeys[mindex].monkeyitems.size(); ++itemindex){
                // parse item
                boost::multiprecision::cpp_int worry = monkeys[mindex].monkeyitems[itemindex];
                // check for "old"
                boost::multiprecision::cpp_int operationnum;
                if(monkeys[mindex].operationnumber == "old"){
                    operationnum = worry;
                } else {
                    operationnum = std::stoi(monkeys[mindex].operationnumber); 
                }
                // apply operation
                if(monkeys[mindex].operationsign == "+"){
                    worry += operationnum;
                } else if(monkeys[mindex].operationsign == "*"){
                    worry *= operationnum;
                }
                // relief
                // worry = (int) worry / 3;
                // check which monkey should get it
                if(worry % monkeys[mindex].monkeydivtestnumber == 0){
                    monkeys[monkeys[mindex].monkeytrue].monkeyitems.emplace_back(worry);
                } else {
                    monkeys[monkeys[mindex].monkeyfalse].monkeyitems.emplace_back(worry);
                }
                // increase inspection count by 1
                ++monkeys[mindex].inspectioncount;
            }
            // clear vector because all items have been moved
            monkeys[mindex].monkeyitems.clear();
        }
    }

    for(auto monkey : monkeys){
        std::cout << monkey.monkeyid << " ";
        for(auto item : monkey.monkeyitems){
            std::cout << item << " ";
        }
        std::cout << "\n";
    }
}
