var currentSlide1=[]
var portfolioChildren1=$('#testimonials-section').children()
var sliderCounter1=0



  function firstRun1()
{
  for (let index = 0; index < currentSlide1.length; index++) {
    $('.testimonial-col').eq(currentSlide1[index]).addClass('slider-animation')
  $('.testimonial-col').eq(currentSlide1[index]).css('display','block')
    
  }
}


function nextSlide1()

{
  portfolioChildren1.css("display",'none')

  console.log("next")
  console.log(currentSlide1)
  if(currentSlide1[currentSlide1.length-1]==portfolioChildren1.length-1)
  {
  console.log("going here")
   for (let index = 0; index < currentSlide1.length; index++) {
     currentSlide1[index]=index  
}
   firstRun1()

  }
 else{
   console.log("going else")
  for (let index = 0; index < currentSlide1.length; index++) {
    currentSlide1[index]=currentSlide1[index]+1
 }
 firstRun1()
}

}

function prevSlide1()

{
  portfolioChildren1.css("display",'none')

  if(currentSlide1[0]==0)
  {
 
   for (let index = portfolioChildren1.length-1; index >= portfolioChildren1.length-currentSlide1.length; index--) {
     currentSlide1[sliderCounter1]=index
     sliderCounter1-=1
}
   firstRun1()
   sliderCounter1=currentSlide1.length-1

  }
 else{

  for (let index = 0; index < currentSlide1.length; index++) {
    currentSlide1[index]=currentSlide1[index]-1
 }
 firstRun1()
}

}

function sliderfirstRun1(slideArray)
{
  currentSlide1=slideArray
portfolioChildren1.css("display",'none')
sliderCounter1=currentSlide1.length-1
firstRun1()
}

if(screen.width <= 600)
{
  sliderfirstRun1([0])
}
else if(screen.width > 600 && screen.width <= 900)
{
  sliderfirstRun1([0,1])
}
else
{
  sliderfirstRun1([0,1,2])
}

 $( window ).resize(function() {
  if(screen.width <= 600)
  {
    sliderfirstRun1([0])
  }
  else if(screen.width > 600 && screen.width <= 900)
  {
    sliderfirstRun1([0,1])
  }
  else
  {
    sliderfirstRun1([0,1,2])
  }
 });
