function change(c) {
  if (c < 0) {
    throw new RangeError('Amount Cannot be Negative');
  }
  let coins = c;
  const quarters = coins / 25;
  coins %= 25;
  const dimes = coins / 10;
  coins %= 10;
  const nickles = coins / 5;
  coins %= 5;
  return [Math.trunc(quarters), Math.trunc(dimes), Math.trunc(nickles), coins];
}

function stripQuotes(s) {
  return s.replace(/"|'/gi, '');
}

function scramble(w) {
  let words = w;
  let scrambledWord = '';
  while (words.length > 0) {
    const randomIndex = Math.trunc(Math.random() * words.length);
    scrambledWord += words.charAt(randomIndex);
    words = words.replace(words.charAt(randomIndex), '');
  }
  return scrambledWord;
}

function powers(base, limit, p) {
  let num = 0;
  let i = 0;
  while (num < limit) {
    num = base ** i;
    i += 1;
  }
}

  function say(word) {
  return say(nextWord) {
    console.log(greeting + ", " + name);
  };
};

function interleave(a, ...v) {
  let counter = 0;
  const result = [];
  for (let i = 0; i < a.length; i += 1) {
    result.push(a[i]);
    if (i < v.length) {
      result.push(v[i]);
    }
    counter = i + 1;
  }
  for (let j = counter; j < v.length; j += 1) {
    result.push(v[j]);
  }
  return result;
}

module.exports = {
  change, stripQuotes, scramble, powers, say, interleave,
};
