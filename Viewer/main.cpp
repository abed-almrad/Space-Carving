#include "Viewer.hpp"
#include <qapplication.h>
#include <iostream>
using namespace std;

int main(int argc, char **argv) {
  // Read command lines arguments.
    QApplication application(argc, argv);

  // Instantiate the viewer.
    Viewer viewer;
    if(argc != 2){
      cout<< "usage: ./myViewer file_name"<<endl;
      return 0;
    }

    std::string name = argv[1];
    //Setting the path
    viewer.setFile("/home/abed/Documents/ETS_Files/Winter_2022/Computer_Vision/Project/Space_Carving_Project/Space_Carving/Space_Carving_Algorithms/"+name+".txt");

    viewer.setWindowTitle("myViewer");
    
  // Make the viewer window visible on screen.
    viewer.show();

  // Run main loop.
    return application.exec();

}
