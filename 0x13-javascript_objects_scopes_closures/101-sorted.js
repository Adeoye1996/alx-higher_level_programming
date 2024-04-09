#!/usr/bin/node
const { dict } = require('./101-data');

const occurrencesMap = new Map();
for (const userId in dict) {
    const occurrences = dict[userId];
    if (occurrencesMap.has(occurrences)) {
        occurrencesMap.get(occurrences).push(userId);
    } else {
        occurrencesMap.set(occurrences, [userId]);
    }
}

const newDict = Object.fromEntries(occurrencesMap);

console.log(newDict);
