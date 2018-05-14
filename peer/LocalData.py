#!/usr/bin/env python
import json


class LocalData:
	""" Data class containing data structures and methods to interact with them """

	# 'session_id'
	session_id = str()

	# ('ipv4', 'ipv6', 'port')
	tracker = tuple()

	# host management ------------------------------------------------------------
	@classmethod
	def get_tracker(cls) -> tuple:
		return cls.tracker

	@classmethod
	def set_tracker(cls, tracker: tuple) -> None:
		cls.tracker = tracker

	@classmethod
	def get_tracker_ip4(cls) -> str:
		return cls.tracker[0]

	@classmethod
	def get_tracker_ip6(cls) -> str:
		return cls.tracker[1]

	@classmethod
	def get_tracker_port(cls) -> int:
		return cls.tracker[2]
	# -----------------------------------------------------------------------------
