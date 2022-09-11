; Hello World example problem

(define (problem BLOCKS-TUT)

(:domain BLOCKS)

(:objects
    ; the only thing is the `world`
    A B C D E M H
)

(:init
    ; Let's assume that the world can hear us
    (ONTABLE B) (ON A B) 
    (ONTABLE H) (ON M H)
    (ONTABLE D) (ON C D) (ON E C)
    (HANDEMPTY)
    (CLEAR A) (CLEAR E) (CLEAR M)
)

(:goal
    (and
        (ONTABLE A) (ON D A)
        (ONTABLE B) (ON C B) (ON E C)
    )
)
)