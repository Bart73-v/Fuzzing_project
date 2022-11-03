Project directory for Software Security's fuzzing project.

# Fuzzing Project Group 02 
### Felix Mölder, Max Pathuis, Maximilian Pohl, Bart Veldman


## AFL++ installation and usage
### Using Docker
To run a single afl-fuzz thread within a docker container run:
```shell
docker run --name afl -ti -v ${PWD}:/src aflplusplus/aflplusplus
cd /src
cmake -DAFL=ON .
make
afl-fuzz -i ./testcases -o ./afl_output -M main -- ./fuzzing_group_02 @@ ./output.tga
```

To add a parallel thread, also utilizing the ASan sanitiser, open another terminal in the same docker container and run:
```shell
# open another bash in the same docker container
docker exec -it afl bash
cd /src

# start a child thread of afl-fuzz
afl-fuzz -i ./testcases -o ./afl_output -S ASan -- ./fuzzing_group_02_ASan @@ ./output_ASan.tga
```

for MSan
```shell
afl-fuzz -i ./testcases -o ./afl_output -S MSan -- ./fuzzing_group_02_MSan @@ ./output_MSan.tga
```