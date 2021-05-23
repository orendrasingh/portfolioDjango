var graph1 = {
    series: [95, 95, 90, 98,90,70],
    chart: {
    height: 350,
    type: 'radialBar',
  },
  plotOptions: {
    radialBar: {
      offsetY: 0,
      startAngle: 0,
      endAngle: 240,
      hollow: {
        margin: 5,
        size: '30%',
        background: 'transparent',
        image: undefined,
      },
      dataLabels: {
        name: {
          show: false,
        },
        value: {
          show: false,
        }
      }
    }
  },
  colors: ['rgba(0, 143, 251, 0.85)', 'rgba(0, 227, 150, 0.85)', 'rgba(255, 139, 10, 0.85)', 'rgba(255, 69, 96, 0.85)','rgba(0, 143, 251, 0.85)','rgba(0, 227, 150, 0.85)'],
  labels: ['Python', 'Django', 'Javascript', 'Html & Css','Wordpress','React JS'],
  legend: {
    show: true,
    floating: true,
    fontSize: '15px',
    position: 'left',
    offsetX: -16,
    offsetY: -1,
    labels: {
      useSeriesColors: true,
    },
    markers: {
      size: 0
    },
    formatter: function(seriesName, opts) {
      return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
    },
    itemMargin: {
      vertical: 3
    }
  },
  responsive: [{
    breakpoint: 480,
    options: {
      legend: {
          show: true
      }
    }
  }]
  };

  var graph2 = {
    series: [100, 90, 85, 90,90],
    chart: {
    height: 350,
    type: 'radialBar',
  },
  plotOptions: {
    radialBar: {
      offsetY: 0,
      startAngle: 0,
      endAngle: 250,
      hollow: {
        margin: 5,
        size: '30%',
        background: 'transparent',
        image: undefined,
      },
      dataLabels: {
        name: {
          show: false,
        },
        value: {
          show: false,
        }
      }
    }
  },
  colors: ['rgba(0, 143, 251, 0.85)', 'rgba(0, 227, 150, 0.85)', 'rgba(255, 139, 10, 0.85)', 'rgba(255, 69, 96, 0.85)','rgba(0, 143, 251, 0.85)'],
  labels: ['Team Work', 'Linux', 'Drupal', 'Web Scraping','SQL/Mongo'],
  legend: {
    show: true,
    floating: true,
    fontSize: '15px',
    position: 'left',
    offsetX: -16,
    offsetY: -2,
    labels: {
      useSeriesColors: true,
    },
    markers: {
      size: 0
    },
    formatter: function(seriesName, opts) {
      return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
    },
    itemMargin: {
      vertical: 3
    }
  },
  responsive: [{
    breakpoint: 480,
    options: {
      legend: {
          show: true
      }
    }
  }]
  };

  var graph3 = {
    series: [80, 85, 60, 60,60],
    chart: {
    height: 350,
    type: 'radialBar',
  },
  plotOptions: {
    radialBar: {
      offsetY: 0,
      startAngle: 0,
      endAngle: 250,
      hollow: {
        margin: 5,
        size: '30%',
        background: 'transparent',
        image: undefined,
      },
      dataLabels: {
        name: {
          show: false,
        },
        value: {
          show: false,
        }
      }
    }
  },
  colors: ['rgba(0, 143, 251, 0.85)', 'rgba(0, 227, 150, 0.85)', 'rgba(255, 139, 10, 0.85)', 'rgba(255, 69, 96, 0.85)','rgba(0, 143, 251, 0.85)'],
  labels: ['Figma', 'Photoshop', 'Adobe XD', 'Illustrator','Inkscape'],
  legend: {
    show: true,
    floating: true,
    fontSize: '15px',
    position: 'left',
    offsetX: -16,
    offsetY: -2,
    labels: {
      useSeriesColors: true,
    },
    markers: {
      size: 0
    },
    formatter: function(seriesName, opts) {
      return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
    },
    itemMargin: {
      vertical: 3
    }
  },
  responsive: [{
    breakpoint: 480,
    options: {
      legend: {
          show: true
      }
    }
  }]
  };  
  var chart = new ApexCharts(document.querySelector("#chart1"), graph1);
  chart.render();
  var chart = new ApexCharts(document.querySelector("#chart2"), graph2);
  chart.render();
  var chart = new ApexCharts(document.querySelector("#chart3"), graph3);
  chart.render();


  // graph end



// var targete=""
//  window.onload = function() {
//   document.addEventListener('swiped-right', function(e) {
//     targete=e.target
//     prevSlide()
    
//   });
//   document.addEventListener('swiped-left', function(e) {
//     nextSlide()
//   });
//  }
