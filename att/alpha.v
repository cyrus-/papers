
Inductive ILTy : Type :=
  | arrow : ILTy -> ILTy -> ILTy
  | prod : ILTy -> ILTy -> ILTy
  | int : ILTy
  | bool : ILTy.

Inductive Ty_ (kappa : Type) : Type := 
  newty : kappa -> ILTy -> Ty_ kappa.

Inductive Ty : Type :=
  | err : Ty
  | indexed_ty : forall (kappa : Type), Ty_ kappa -> Ty.

Definition idx (kappa : Type) (a : Ty_ kappa) : kappa := 
  match a with 
  | newty idx rep => idx
  end.

Axiom refine : forall (a:Ty) 
                      (kappa out : Type) 
                      (transfer : Ty_ kappa -> out) 
                      (default : out), out.

Axiom refine_err : forall (x : Ty), 
  (x = err) -> forall (kappa out : Type) 
                      (transfer : Ty_ kappa -> out) 
                      (default : out), 
    (refine x kappa out transfer default = default).

Axiom refine_indexed : forall (x : Ty) (kappa : Type) (t : Ty_ kappa),
  (x = indexed_ty kappa t) -> forall (out : Type)
                                     (transfer : Ty_ kappa -> out)
                                     (default : out), 
    (refine x kappa out transfer default = transfer t).


