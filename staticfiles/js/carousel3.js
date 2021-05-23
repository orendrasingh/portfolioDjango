var currentSlide2=[]
var portfolioChildren2=$('#portfolio-inner2').children()
var sliderCounter2=0



  function firstRun2()
{

  for (let index = 0; index < currentSlide2.length; index++) {
   $('.portfolio-count-2').eq(currentSlide2[index]).addClass('slider-animation')
    $('.portfolio-count-2').eq(currentSlide2[index]).css('display','flex')
 
    
  }
}


function nextSlide2()

{
  portfolioChildren2.css("display",'none')

  console.log("next")
  console.log(currentSlide2)
  if(currentSlide2[currentSlide2.length-1]==portfolioChildren2.length-1)
  {
  console.log("going here")
   for (let index = 0; index < currentSlide2.length; index++) {
     currentSlide2[index]=index  
}
   firstRun2()

  }
 else{
   console.log("going else")
  for (let index = 0; index < currentSlide2.length; index++) {
    currentSlide2[index]=currentSlide2[index]+1
 }
 firstRun2()
}

}

function prevSlide2()

{
  portfolioChildren2.css("display",'none')

  if(currentSlide2[0]==0)
  {
 
   for (let index = portfolioChildren2.length-1; index >= portfolioChildren2.length-currentSlide2.length; index--) {
     currentSlide2[sliderCounter2]=index
     sliderCounter2-=1
}
   firstRun2()
   sliderCounter2=currentSlide2.length-1

  }
 else{

  for (let index = 0; index < currentSlide2.length; index++) {
    currentSlide2[index]=currentSlide2[index]-1
 }
 firstRun2()
}

}


function sliderfirstRun2(slideArray)
{
  currentSlide2=slideArray
portfolioChildren2.css("display",'none')
sliderCounter2=currentSlide2.length-1
firstRun2()
}



if(screen.width <= 600)
{
  sliderfirstRun2([0])
}
else if(screen.width > 600 && screen.width <= 900)
{
  sliderfirstRun2([0])
}
else
{
  sliderfirstRun2([0,1])
}

 $( window ).resize(function() {
  if(screen.width <= 600)
  {
    sliderfirstRun2([0])
  }
  else if(screen.width > 600 && screen.width <= 900)
  {
    sliderfirstRun2([0,1,2])
  }
  else
  {
    sliderfirstRun2([0,1,2,3])
  }
 });
