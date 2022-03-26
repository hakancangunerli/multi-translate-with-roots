#include <iostream>
#include <string>
#include "LibreTranslate.h"
using namespace std; 


string translateInput; 
int main(){
 LibreTranslateAPI libreTranslateAPI;
   cout << "Text to be translated:";
  getline(cin, translateInput);
  string multiLang[3] = {"de", "fr", "es"};
  for (int i = 0; i < 3; i++) {
    cout << libreTranslateAPI.translate(translateInput, "en", multiLang[i]) << std::endl;
  }
  return 0;
}
