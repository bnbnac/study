const quotes = [
    {
        quote : "yes, the cyclic",
        author : "mj",
    },
    {
        quote : "i will be 3bill",
        author : "sj",
    },
    {
        quote : "it can be",
        author : "mo",
    },
    {
        quote : "oh my god",
        author : "mother",
    },
    {
        quote : "...",
        author : "father",
    },
]

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

todaysQuote = quotes[Math.floor(Math.random()*quotes.length)];


quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;