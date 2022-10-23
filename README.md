Project directory for Software Security's fuzzing project.

# Fuzzing Project Group 02 
### Felix Mölder, Max Pathuis, Maximilian Pohl, Bart Veldman


## AFL++ installation and usage
### Using Docker
```shell
docker run -ti -v ${PWD}:/src aflplusplus/aflplusplus
cd ../src
cmake -DAFL=ON .
make
afl-fuzz -i ./testcases -o ./afl_output -- ./fuzzing_group_02 @@ ./output.tga
```