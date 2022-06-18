{ pkgs ? import <nixpkgs> { }
, pkgsLinux ? import <nixpkgs> { system = "x86_64-linux"; }
}:

pkgs.dockerTools.buildImage {
  name = "take-my-form";
  config = {
    FROM = "python:3.9";
    WORKDIR = "/code";
    COPY = "./requirements.txt /code/requirements.txt";
    RUN = "pip install --no-cache-dir --upgrade -r /code/requirements.txt";
    COPY = "./app /code/app";
    Cmd = [ "uvicorn" "app.main:app" "--proxy-headers" "--host" "0.0.0.0" "--port" "80" ];
  };
}