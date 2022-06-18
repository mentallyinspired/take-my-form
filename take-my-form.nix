{ pkgs ? import <nixpkgs> { }
, pkgsLinux ? import <nixpkgs> { system = "x86_64-linux"; }
}:

pkgs.dockerTools.buildImage {
  name = "take-my-form";
  tag = lates;
  runAsRoot = ''
    mkdir /code
    cp ./requirements.txt /code/requirements.txt
    pip install --no-cache-dir --upgrade -r /code/requirements.txt
    cp ./app /code/app
  '';


  config = {
    FROM = "python:3.10";
    WORKDIR = "/code";
    Cmd = [ "uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 8095" ];
  };
}