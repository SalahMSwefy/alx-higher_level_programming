#!/usr/bin/node
const args = process.argv;
args.sort((a, b) => a - b);
console.log(args[args.length - 2]);
