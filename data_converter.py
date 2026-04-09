import numpy as np
import scipy.io 


# convert 3d .mat file to 2d array to store it in .h file so we can use it in cpp file.

def convert_mat_to_h( mat_file, h_file, elevation=12):
    data=scipy.io.loadmat(mat_file)
    print(data.keys())

    hrir_l=data['hrir_l']
    hrir_r=data['hrir_r']

    print(hrir_l.shape)
    print(hrir_r.shape)

    left=[]
    right=[]
    
    #length of azimuthal angles  25 so 0 to 24
    # we fixed the elevation angle to 0 degree so we only need to 
    # convert the data for that elevation angle which is at 
    # index 0 in the 3rd dimension of the hrir_l and hrir_r arrays.

    left=np.array(hrir_l[:,elevation,:128])
    right=np.array(hrir_r[:,elevation,:128])

    # normalize the left and right arrays to be between -1 and 1
    left=left/np.max(np.abs(left))
    right=right/np.max(np.abs(right))

    print(left.shape)
    print(right.shape)

    # save the left and right arrays in .h file
    # if file not found create it and write the data in it
    with open(output_h_file, 'w') as f:
        f.write('#ifndef HRIR_DATA_H\n')
        f.write('#define HRIR_DATA_H\n\n')
        f.write('const int num_azimuths = 25;\n')
        f.write('const int num_samples = 128;\n\n')
        f.write('float hrir_l[num_azimuths][num_samples] = {\n')
        for i in range(left.shape[0]):
            f.write('    {')
            for j in range(left.shape[1]):
                f.write(f'{left[i][j]}f')
                if j < left.shape[1] - 1:
                    f.write(', ')
            f.write('}')
            if i < left.shape[0] - 1:
                f.write(',\n')
            else:
                f.write('\n')
        f.write('};\n\n')

        f.write('float hrir_r[num_azimuths][num_samples] = {\n')
        for i in range(right.shape[0]):
            f.write('    {')
            for j in range(right.shape[1]):
                f.write(f'{right[i][j]}f')
                if j < right.shape[1] - 1:
                    f.write(', ')
            f.write('}')
            if i < right.shape[0] - 1:
                f.write(',\n')
            else:
                f.write('\n')
        f.write('};\n\n')

        f.write('#endif // HRIR_DATA_H\n')


input_mat_file='E:\HRTF\HRTF_code\cipic-hrtf-database-master\standard_hrir_database\subject_003\hrir_final.mat'
output_h_file='hrir_data1.h'
convert_mat_to_h(input_mat_file,output_h_file,)

    