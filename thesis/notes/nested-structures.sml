signature A = sig
  type t
end

signature B = sig
  type u
  structure S : A
end

structure M :> A = struct
  type t = int
end

structure N :> B = struct
  type u = string
  structure S = M
end

structure N' : B = struct
  type u = string
  structure S = M
end

fun g(x : N.S.t) = x;
fun f(x : M.t -> M.t) = x;
(* doesn't work:
f(g);
*)

(* but this does: *)
fun g'(x : N'.S.t) = x;
f(g');

(* so, what's happening?
*
* opaque ascription leaves types abstract, but also structures.
* or can we just unify this as opaque ascription prevents type equalities from
* propagating out. *)

signature C = sig
  type u
  structure S : A = M
end

structure N'' :> C = struct
  type u = string
  structure S = M
end

fun g''(x : N''.S.t) = x;
f(g'');

(* type and structure equalities:
*
* for N, you only know that there exists a type u and a structure S.
*)

