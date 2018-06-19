@echo off
FOR /R tbmgr\tbapi\protos %%i IN (*.proto) DO (
    protoc -I="%CD%\tbmgr\tbapi\protos" --python_out=tbmgr\tbapi\pyprotos %%i
)
