;; Auto-generated. Do not edit!


(when (boundp 'motor_controller::IntList)
  (if (not (find-package "MOTOR_CONTROLLER"))
    (make-package "MOTOR_CONTROLLER"))
  (shadow 'IntList (find-package "MOTOR_CONTROLLER")))
(unless (find-package "MOTOR_CONTROLLER::INTLIST")
  (make-package "MOTOR_CONTROLLER::INTLIST"))

(in-package "ROS")
;;//! \htmlinclude IntList.msg.html


(defclass motor_controller::IntList
  :super ros::object
  :slots (_wheel _arm _hopper _bucket ))

(defmethod motor_controller::IntList
  (:init
   (&key
    ((:wheel __wheel) (make-array 0 :initial-element 0 :element-type :integer))
    ((:arm __arm) (make-array 0 :initial-element 0 :element-type :integer))
    ((:hopper __hopper) (make-array 0 :initial-element 0 :element-type :integer))
    ((:bucket __bucket) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _wheel __wheel)
   (setq _arm __arm)
   (setq _hopper __hopper)
   (setq _bucket __bucket)
   self)
  (:wheel
   (&optional __wheel)
   (if __wheel (setq _wheel __wheel)) _wheel)
  (:arm
   (&optional __arm)
   (if __arm (setq _arm __arm)) _arm)
  (:hopper
   (&optional __hopper)
   (if __hopper (setq _hopper __hopper)) _hopper)
  (:bucket
   (&optional __bucket)
   (if __bucket (setq _bucket __bucket)) _bucket)
  (:serialization-length
   ()
   (+
    ;; int32[] _wheel
    (* 4    (length _wheel)) 4
    ;; int32[] _arm
    (* 4    (length _arm)) 4
    ;; int32[] _hopper
    (* 4    (length _hopper)) 4
    ;; int32[] _bucket
    (* 4    (length _bucket)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _wheel
     (write-long (length _wheel) s)
     (dotimes (i (length _wheel))
       (write-long (elt _wheel i) s)
       )
     ;; int32[] _arm
     (write-long (length _arm) s)
     (dotimes (i (length _arm))
       (write-long (elt _arm i) s)
       )
     ;; int32[] _hopper
     (write-long (length _hopper) s)
     (dotimes (i (length _hopper))
       (write-long (elt _hopper i) s)
       )
     ;; int32[] _bucket
     (write-long (length _bucket) s)
     (dotimes (i (length _bucket))
       (write-long (elt _bucket i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _wheel
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _wheel (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _wheel i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _arm
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _arm (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _arm i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _hopper
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _hopper (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _hopper i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _bucket
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bucket (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _bucket i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get motor_controller::IntList :md5sum-) "4e62f442e2d55a264cd175bb6226f3c7")
(setf (get motor_controller::IntList :datatype-) "motor_controller/IntList")
(setf (get motor_controller::IntList :definition-)
      "int32[] wheel
int32[] arm
int32[] hopper
int32[] bucket

")



(provide :motor_controller/IntList "4e62f442e2d55a264cd175bb6226f3c7")


