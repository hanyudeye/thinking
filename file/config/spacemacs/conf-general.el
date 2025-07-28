(setq-default
 evil-escape-key-sequence "kj"
 evil-escape-delay 0.5

 ;; sdcv 词典配置
 ;; sdcv-popup-function 'popup-tip
 ;; sdcv-popup-function 'tooltip-show
 ;; sdcv-popup-function 'pos-tip-show
 ;;不发音
 ;; sdcv-word-pronounce nil
 sdcv-fail-notify-string nil

 eww-search-prefix "https://bing.com/search?q="

 ;; 解压缩
;; nov-unzip-program (executable-find "d:/Program Files/Git/usr/bin/unzip.exe")
 )

;; 添加代码片段目录
(add-to-list 'yas-snippet-dirs my-snippet-path)
;; 取消光标所在行的高亮
;; (global-hl-line-mode -1)
;;snippet
;; (setq my-snippet "/home/wuming/.spacemacs.d/snippets")
;; (add-to-list 'yas-snippet-dirs my-snippet)

;; (defun find-org-passwd()
;;   (interactive)
;;   (find-file "/home/wuming/me/config/passwd/passwd.org")
;;   )

;; (evil-leader/set-key "o o p" 'find-org-passwd)
;;sdcv 翻译
(evil-leader/set-key "o s" 'sdcv-search-pointer+)

(provide 'conf-general)
