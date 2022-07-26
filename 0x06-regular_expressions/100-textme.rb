#!/usr/bin/env ruby

sender = ARGV[0].scan(/(?=from:(\+?\w+))/)
rec = ARGV[0].scan(/(?=to:(\+?\w+))/)
flags = ARGV[0].scan(/(?=flags:(\-?\d:\-?\d:\-?\d:\-?\d:\-?\d))/)
text = sender + rec + flags
puts text.join(",")
