import FCMManager as fcm

tokens = ["AAAAHJcqDUc:APA91bEbUMOcz0FwzvLDTzweJrrhyzqu7fYwLHSPF0EnaRuCjwaTHDM3-RxGlnK_pWA2SZWFr1i5cN3u5jIh1q9pZ5Pi-imHfiOTzXYUbeCKTN4-6ixtfD1xHtaLaWizjNXwdSPUdN8I"]
fcm.sendPush("Hi", "This is my next msg", tokens)