let data = {};
let corpusData = {}
       fetch("/api/zipf_stats")
          .then(response => response.json())
          .then(d => { data = d; loadStats(); });

       fetch("/api/corpus_stats")
          .then(response => response.json())
          .then(d => { corpusData = d; loadCorpusStats(); });
function loadStats() {
      let button = document.getElementById("average-btn")
      button.innerHTML = `<b>Average:</b> ${data.average.toFixed(2)}`;
      button = document.getElementById("stddev-btn")
      button.innerHTML = `<b>Standard Deviation:</b> ${data.stddev.toFixed(2)}`;
      button = document.getElementById("variance-btn")
      button.innerHTML = `<b>Variance:</b> ${data.variance.toFixed(2)}`;
    }
function loadCorpusStats() {
      let paragraph = document.getElementById("corpus_stats")
      paragraph.innerHTML =
          `<b>Corpus contains: </b></br>
          - <b>${corpusData.articles}</b> words from Wikipedia articles </br>
          - <b>${corpusData.OtherArticles}</b> words from other Creative Commons articles </br>
          - <b>${corpusData.novels}</b> words from novels such as 1984 by George Orwell </br> and O crime do padre Amaro... by Eça de Queirós </br>
          <b>${corpusData.all}</b> words totally`



    }
