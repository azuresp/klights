docker build -t opencvtest ./docker 
docker run --rm --mount type=bind,source=d:/temp/output,destination=/dump -t opencvtest 