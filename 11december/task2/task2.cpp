#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm> 
#include <cctype>
#include <locale>

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
    for(int i = 0; i < lines.size(); i += 6){
        // id of monkey, should be unique from input counting up from 0
        int monkeyid = std::stoi(util::replace(util::split(lines.at(i), " ").at(1), ";", ""));    
        // items
        std::vector<std::string> partsitems = util::split(lines.at(i + 1), " ");
        std::vector<int> items;
        for(int j = 2; j < partsitems.size(); ++j){
            items.emplace_back(std::stoi(partsitems[j]));
        }
        // operation
        std::string operationsign = util::split(lines.at(i + 2), " ").at(4);
        int operationnumber = std::stoi(util::split(lines.at(i + 2), " ").at(5));
        // test and possible monkeys to transfer item to
        int monkeydivtestnumber = std::stoi(util::split(lines.at(i + 3), " ").at(lines.size() - 1));
        int monkeytrue = std::stoi(util::split(lines.at(i + 4), " ").at(lines.size() - 1));
        int monkeyfalse = std::stoi(util::split(lines.at(i + 5), " ").at(lines.size() - 1));
    }
}
