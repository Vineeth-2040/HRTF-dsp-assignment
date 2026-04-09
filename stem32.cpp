#include"hrir_data1.h"
#include <iostream>


int main(){
    # print first 2 rows of the dataset to check if it is correct
    for(int i=0;i<2;i++){
        std::cout<<"Azimuth "<<i<<":\n";
        std::cout<<"Left: ";
        for(int j=0;j<num_samples;j++){
            std::cout<<hrir_l[i][j]<<" ";
        }
        std::cout<<"\nRight: ";
        for(int j=0;j<num_samples;j++){
            std::cout<<hrir_r[i][j]<<" ";
        }
        std::cout<<"\n\n";
    }
}
