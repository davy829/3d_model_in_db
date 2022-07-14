function preload(){
    gun = loadModel('./car.obj',true)
  }
  function setup(){
    createCanvas(windowWidth,windowHeight,WEBGL)
  }
  function draw(){
    background('LIGHTBLUE')
    scale(2)
    rotateZ(millis() / 10000)
    rotateY(millis() / 10000)
    rotateX(millis() / 10000)
    normalMaterial()//for colors
    model(gun)
  }
  function windowResized(){
    resizeCanvas(windowWidth,windowHeight)
  }
console.log(1)