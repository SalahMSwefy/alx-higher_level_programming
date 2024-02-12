#!/usr/bin/node
const nums = process.argv.length;
const args = process.argv;
args.sort((a, b) => a - b);
if (nums < 4) {
  console.log(0);
} else {
  console.log(args[args.length - 2]);
}
