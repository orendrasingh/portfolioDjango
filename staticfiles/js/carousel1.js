var currentSlide=[]
var portfolioChildren=$('#portfolio-inner').children()
var sliderCounter=0



  function firstRun()
{

  for (let index = 0; index < currentSlide.length; index++) {
   $('.portfolio-count-1').eq(currentSlide[index]).addClass('slider-animation')
    $('.portfolio-count-1').eq(currentSlide[index]).css('display','flex')
 
    
  }
}


function nextSlide()

{
  portfolioChildren.css("display",'none')

  console.log("next")
  console.log(currentSlide)
  if(currentSlide[currentSlide.length-1]==portfolioChildren.length-1)
  {
  console.log("going here")
   for (let index = 0; index < currentSlide.length; index++) {
     currentSlide[index]=index  
}
   firstRun()

  }
 else{
   console.log("going else")
  for (let index = 0; index < currentSlide.length; index++) {
    currentSlide[index]=currentSlide[index]+1
 }
 firstRun()
}

}

function prevSlide()

{
  portfolioChildren.css("display",'none')

  if(currentSlide[0]==0)
  {
 
   for (let index = portfolioChildren.length-1; index >= portfolioChildren.length-currentSlide.length; index--) {
     currentSlide[sliderCounter]=index
     sliderCounter-=1
}
   firstRun()
   sliderCounter=currentSlide.length-1

  }
 else{

  for (let index = 0; index < currentSlide.length; index++) {
    currentSlide[index]=currentSlide[index]-1
 }
 firstRun()
}

}


function sliderFirstRun(slideArray)
{
  currentSlide=slideArray
portfolioChildren.css("display",'none')
sliderCounter=currentSlide.length-1
firstRun()
}



if(screen.width <= 600)
{
  sliderFirstRun([0])
}
else if(screen.width > 600 && screen.width <= 900)
{
  sliderFirstRun([0])
}
else
{
  sliderFirstRun([0,1])
}

 $( window ).resize(function() {
  if(screen.width <= 600)
  {
    sliderFirstRun([0])
  }
  else if(screen.width > 600 && screen.width <= 900)
  {
    sliderFirstRun([0,1,2])
  }
  else
  {
    sliderFirstRun([0,1,2,3])
  }
 });
