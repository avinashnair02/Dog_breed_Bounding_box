console.log('WORKING')

function ssubmit(){
    console.log('CLICKED ON SUBMIT')
    const loadingEl = document.getElementById('load_cont')
     loadingEl.style.display = 'flex'
    const imageEl = document.getElementById('img_cont')
    imageEl.style.display = 'none'
   
}


var elemets = document.querySelector('svg').children;

anime({
  targets: 'line',
  translateX: [
    {value: 270, duration: 1000, easing: 'easeOutSine'},
    {value: 0, duration: 1000, easing: 'easeOutSine'}
  ],
  delay: anime.stagger(200, {grid: [16,10], from: 7}),
  loop: true
})


